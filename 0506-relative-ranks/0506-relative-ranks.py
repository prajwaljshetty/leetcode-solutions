class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranks = ["Gold Medal","Silver Medal","Bronze Medal"]
        placeMap = {}
        for index , scoreI in enumerate(sorted(score , reverse=True)) :
            if index < len(ranks) : placeMap[scoreI] = ranks[index]
            else : placeMap[scoreI] = f"{index + 1}"
        return [placeMap[scoreI] for scoreI in score]