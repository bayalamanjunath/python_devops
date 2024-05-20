#https://medium.com/@mohamedabdelazizk10/complete-end-to-end-devsecops-kubernetes-three-tier-project-using-aws-eks-argocd-prometheus-0f1cfdcfe4c3
import sys
n = int(sys.argv[1])
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(factorial)
