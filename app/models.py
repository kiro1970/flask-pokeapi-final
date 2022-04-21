from app import db

class BattleDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    YourPokemon = db.Column(db.String(100))
    OpponentsPokemon = db.Column(db.String(100))
    Winner = db.Column(db.String(10))

    def __repr__(self):
        return f'id {self.id} {self.YourPokemon} {self.OpponentsPokemon} {self.Winner}'
