//  ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

function solution(n, times) {
    //times는 오름차순으로 정렬.
    const sortedTimes = times.sort((a, b) => a - b);
    let leftTarget = 1;
    let rightTarget = sortedTimes[sortedTimes.lenth - 1] * n;

    while (leftTarget <= rightTarget) {
        let mid = Math.floor((leftTarget + rightTarget) / 2);
        let cnt = 0;
        let result = 10000000000;

        for (let i = 0; i < sortedTimes.lenth; i++) {
            cnt += Math.floor(mid / sortedTimes[i]);
        }
        if (cnt > n) {
            rightTarget = mid - 1;
        }
        if (cnt < n) {
            leftTarget = mid + 1;
        }
        if (result > mid) {
            result = mid;
        }
    }
    return result;
}

// # ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
// # 풀이:

// # 문제:

// # 해결:

// # 느낀점:
