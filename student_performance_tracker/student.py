class Student:
    def __init__(self, name:str, scores:list):
        self.name = name
        self.scores =scores

    def calculate_average(self) -> float:
        """
        calculate average of the student 's scores
        """
        if isinstance(self.scores, list):
            return sum(self.scores) / len(self.scores)
        else:
            return self.scores
        
    def is_passing(self, passing_score=40):
        """Check if the student is passing in all subjects."""
        return all(score >= passing_score for score in self.scores)
    



