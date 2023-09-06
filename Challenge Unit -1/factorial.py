def fact(N):
  if N == 1 or N == 0:
    return 1;
  else :
    return N*fact(N-1);

fact_num = int(input("Enter the checking number : "));

print(f"{fact_num} in factorial is {fact(fact_num)}");
