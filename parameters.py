class Parameters:

    def __init__(self, village_code, village_name, voters, envelopes, votes, parties):
        self.code = village_code
        self.name = village_name
        self.voters = voters
        self.envelopes = envelopes
        self.votes = votes
        self.parties = parties

    def __str__(self):
        return (f"Parameters(code={self.code}, name={self.name}, voters={self.voters}, "
                f"envelopes={self.envelopes}, votes={self.votes}, parties={self.parties})")