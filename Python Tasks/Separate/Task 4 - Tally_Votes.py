from collections import Counter

def tally_votes():
    # Ask for votes until the user decides to finish
    votes = iter(lambda: input("Enter a vote (or -1 to finish): "), "-1")
    votes_count = Counter(votes)

    # Check if any votes were cast
    if len(votes_count) == 0:
        print("No votes were cast.")
    else:
        # Find the maximum number of votes
        max_votes = max(votes_count.values())
        # Find the candidates with the maximum votes (potential winners)
        winners = [candidate for candidate, vote_count in votes_count.items() if vote_count == max_votes]

        # Display the vote tally for all candidates
        print("Vote tally:")
        for candidate, vote_count in votes_count.items():
            print(f"{candidate}: {vote_count} votes")

        # Check if there is a single winner or a tie
        if len(winners) == 1:
            # Display the winner's name and vote count
            print(f"The winner is {winners[0]} with {max_votes} votes.")
        else:
            # Display the tied winners' names and vote count
            print("It's a tie! The winners are:")
            for winner in winners:
                print(f"{winner} with {max_votes} votes.")

tally_votes()