function Factorial(n)
  if n == 1 then
    return 1
  else
    return n * Factorial(n - 1)
  end
end

function Main()
  print(Factorial(5))
end

Main()
