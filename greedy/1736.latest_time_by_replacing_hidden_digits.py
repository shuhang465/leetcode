class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == '?':
            time[0] = '2' if time[1] in ('0','1','2','3','?') else '1'
        if time[1] == '?':
            time[1] = '9' if time[0] in ('0','1') else '3'
        if time[3] == '?': time[3] = '5'
        if time[4] == '?': time[4] = '9'
        return "".join(time)
