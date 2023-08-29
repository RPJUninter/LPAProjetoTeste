from code.Constant import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_window_colission(ent: Entity):
        if isinstance(ent, Enemy) and ent.rect.right < 0:
            ent.health = 0
            return 'window'
        elif isinstance(ent, EnemyShot) and ent.rect.right < 0:
            ent.health = 0
            return 'window'
        elif isinstance(ent, PlayerShot) and ent.rect.left > WIN_WIDTH:
            ent.health = 0
            return 'window'
        else:
            return None

    @staticmethod
    def verify_colission(entity_list: list[Entity]):
        for ent in entity_list:
            ent.last_hit = EntityMediator.__verify_window_colission(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
