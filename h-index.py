class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        #sort the array in descending order
        citations.sort(reverse = True)
        for i in range(len(citations)):
        # i represents the current index (0-based)
        # i + 1 represents the number of papers we're considering
        # citations[i] is the number of citations for the current paper
        
        # We're checking if the number of papers (i + 1) is greater than or equal to
        # the number of citations for the current paper
        
            if i>=citations[i]:
                # If true, we've found the h-index
            # i papers have at least i citations each
                return i
        return len(citations)