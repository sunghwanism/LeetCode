class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # 공집합도 하나의 BST로 봄

        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1        # 왼쪽 서브트리 노드 수
                right = nodes - root  # 오른쪽 서브트리 노드 수
                dp[nodes] += dp[left] * dp[right]

        return dp[n]





        