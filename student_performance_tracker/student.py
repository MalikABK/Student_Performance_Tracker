class Student:
    def __init__(self, name:str, scores:list):
        self.name = name
        self.scores =scores

    def calculate_average(self) -> float:
        if not self.scores:  # Avoid division by zero
            return 0
        average:float = sum(self.scores)  / len(self.scores)  
        return average
        

    # def is_passing(self):        
    #     is_pass = "Pass"  # Initialize to "Pass"
    #     for score in self.scores:
    #         if score < 40:  # Check if any score is below 40
    #             is_pass = "Fail"  # Change to "Fail" if condition met
    #             break  # Exit loop since one fail is enough            
    #       # Print final result
    #     return is_pass
    # def is_passing(self, passing_score=40):
    #     """Check if the student is passing in all subjects."""
    #     return all(score >= passing_score for score in self.scores)

    # def failed_subjects(self, passing_score=40):
    #     """Return a list of scores that are below the passing score."""
    #     return [score for score in self.scores if score < passing_score]
    
    def is_passing(self, passing_score=40):
        """Check if the student is passing in all subjects."""
        return all(score >= passing_score for score in self.scores)
    



