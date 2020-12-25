class Game:
    def __init__(self,id):
        self.p1gone = False
        self.p2gone = False
        self.ready = False
        self.id = id
        self.moves = [None,None]
        self.wins = [0,0]
        self.ties = 0
        self.winning_dict = {'RR':0,'SS':0,'PP':0,'RS':1,'SR':-1,'RP':-1,'PR':1,'SP':1,'PS':-1}
    def get_player_move(self,p):
        """

        :param p: [0,1]
        :return:
        """
        return self.moves[p]

    def player(self,player,move):
        self.moves[player] = move
        if player == 0:
            self.p1gone = True
        if player ==1:
            self.p2gone = True

    def connected(self):
        return self.ready

    def both_gone(self):
        return self.p1gone and self.p2gone

    def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]
        key = p1+p2
        return self.winning_dict[key]

    def reset_gone(self):
        self.p1gone=False
        self.p2gone=False
