import csv

class Scores:
    def __init__(self):
        self.file = 'Students_scores.csv'
        self.setup_file()

    def setup_file(self):
        try:
            with open(self.file, 'x', newline='') as file:
                csv.writer(file).writerow(['Student Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4',
                                           'Final Score', 'Highest Score', 'Lowest Score', 'Average Score'
                                           ])
        except FileExistsError:
            pass

    def save_scores(self, name, attempts, score_input):
        if not name.strip():
            return 'Missing name', False
        if not attempts.isdigit() or int(attempts) not in {1, 2, 3, 4}:
            return 'Enter 1-4 attempts', False

        scores = []
        for x in range(int(attempts)):
            try:
                score = float(score_input[x])
                if score < 0 or score > 100:
                    return f'Score {x+1} must be from 0 to 100', False
                scores.append(score)
            except (ValueError, IndexError):
                return f'Invalid Score {x+1} entered', False


        while len(scores) < 4:
            scores.append(0.0)

        high = max(scores)
        low = min(scores)
        average = sum(scores) / 4
        final = high

        row_data = [name, *scores, final, high, low, round(average, 2)]

        with open(self.file, 'a', newline='') as file:
            csv.writer(file).writerow(row_data)

        return 'Scores saved successfully', True

