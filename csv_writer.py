import csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, parameters_list):
        """Export list of Parameters objects to CSV file."""
        with open(self.filename, mode='w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            # Write header
            headers = ['Code', 'Name', 'Voters', 'Envelopes', 'Votes']

            parties = [name for name, vote in parameters_list[0].parties] 
            headers.extend(parties)
            writer.writerow(headers)
            # Write data
            for param in parameters_list:
                # Flatten parties dict for CSV
                votes = [vote for name, vote in param.parties]
                row= [param.code, param.name, param.voters, param.envelopes, param.votes, ]
                row.extend(votes)
                writer.writerow(row)


