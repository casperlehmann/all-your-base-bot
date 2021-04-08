from random import randint
import random
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.unit import Unit, UnitTypeId
from sc2.units import Units
from sc2.position import Point2
from sc2.constants import AbilityId

class MarineRushBot(sc2.BotAI):

    _builder_unit_tag: str = None

    async def on_step(self, iteration: int):
        if iteration == 0:
            self.train(UnitTypeId.SCV, 1)
        
        if (len(self.structures(UnitTypeId.SUPPLYDEPOT)) == 0) or (self.supply_left < 3 and self.supply_cap != 200):
            await self.build_supply_depot()

        if (len(self.structures(UnitTypeId.REFINERY)) < 1):
            await self.take_gas()

        if iteration % 3 == 0:
            # Train an SCV from a random idle command center
            cc = self.townhalls.idle.random_or(None)
            # self.townhalls can be empty or there are no idle townhalls
            if cc and self.can_afford(UnitTypeId.SCV) and len(self.workers) < 80:
                print(f'Train SCV ({len(self.workers)})')
                cc.train(UnitTypeId.SCV)
            await self.distribute_workers()

        if iteration % 5 == 0:
            if self.can_afford(UnitTypeId.BARRACKS):
                await self.build_barracks()

        if iteration % 6 == 0:
            for barracks in self.structures.filter(lambda structure: structure.name == 'Barracks').idle:
                if self.can_afford(UnitTypeId.MARINE):
                    barracks.train(UnitTypeId.MARINE)
                if self.can_afford(UnitTypeId.MARINE):
                    barracks.train(UnitTypeId.MARINE)
        
        if iteration % 3 == 0 and self.can_afford(UnitTypeId.COMMANDCENTER) and len(self.townhalls) < 12:
            await self.expand_now()

        if iteration % 5000 == 0 or self.supply_cap > 160:
            for marine in self.units(UnitTypeId.MARINE):
                if self.enemy_structures:
                    target = random.choice(self.enemy_structures).position
                    marine.attack(target)
                    #marine.attack(Point2.random_on_distance(marine.position, 500))
    
    async def build_supply_depot(self):
        if self.already_pending(UnitTypeId.SUPPLYDEPOT) >= 1:
            return
        if self.townhalls:
            cc = self.townhalls[0]
            depot_position = await self.find_placement(UnitTypeId.SUPPLYDEPOT, near=cc.position)
        else:
            print("You're already dead.")
            return
        if not depot_position:
            print (f"CAN'T BUILD THERE! near={cc.position}")
            return
        builder = await self.get_or_assign_builder(location = depot_position)
        if builder:
            builder.build(UnitTypeId.SUPPLYDEPOT, depot_position)
        else:
            print ('No builder selected :(')

    async def take_gas(self):
        builder = await self.get_or_assign_builder(self.main_base_ramp.barracks_correct_placement)
        geyser = self.vespene_geyser.closest_to(builder)
        #if geyser.has_reactor:
        builder.build(UnitTypeId.REFINERY, position=geyser)
        return

    async def build_barracks(self):
        if self.already_pending(UnitTypeId.BARRACKS) >= 1:
            return
        print('Build Barracks')
        barracks_placement_position = self.main_base_ramp.barracks_correct_placement
        builder = await self.get_or_assign_builder(location = barracks_placement_position)
        if builder:
            assert isinstance(barracks_placement_position, Point2)
            new_position = await self.find_placement(UnitTypeId.BARRACKS, near=barracks_placement_position)
            builder.build(UnitTypeId.BARRACKS, new_position)
        else:
            print ('No builder selected :(')
    
    async def get_or_assign_builder(self, location: Point2):
        if self._builder_unit_tag:
            builder = Units.find_by_tag(self.units, self._builder_unit_tag)
            if builder:
                if not builder.is_constructing_scv:
                    return builder
        builder = self.select_build_worker(pos = location)
        self._builder_unit_tag = builder.tag
        return builder
    
    async def on_unit_created(self, unit: Unit):
        print(f'Build {unit} {unit.type_id}')
        if unit.type_id == UnitTypeId.MARINE:
            if self.units_created[UnitTypeId.MARINE] % 10 == 0:
                for marine in self.units(UnitTypeId.MARINE):
                    if randint(1, 20) == 1:
                        marine.attack(Point2.random_on_distance(marine.position, 500))
                    else:
                        marine.attack(self.enemy_start_locations[0])
    
    async def on_building_construction_complete(self, unit: Unit):
        print(f"unit.type_id: {unit.type_id}")
        if unit.type_id == UnitTypeId.BARRACKS:
            if not unit.has_reactor:
                print(f'Buildreactor')
                print(unit.build(UnitTypeId.BARRACKSREACTOR))

    async def on_building_construction_started(self, unit: Unit):
        if unit.type_id == UnitTypeId.COMMANDCENTER:
            unit(AbilityId.RALLY_WORKERS, self.mineral_field.closest_to(unit))
        
    
    async def on_unit_destroyed(self, unit_tag: int):
        print(f'Unit died: RIP Comrade {unit_tag}.')

run_game(
    maps.get("Acropolis LE"),
    [
        Bot(Race.Terran, MarineRushBot()),
        Computer(Race.Protoss, Difficulty.Medium)
    ],
    realtime=True
)
