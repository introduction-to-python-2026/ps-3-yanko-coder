def approximate_pi(n_terms):
  pi_est = 0
  for i in range(0,n_terms):
    pi_est += ((-1)**i)/(2*i+1)
  result = pi_est * 4
  print(result)

approximate_pi(1000)
