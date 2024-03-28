function LengthConvert(choice, value)
  if choice == 1 then
    return value / 1.60934
  else
    return value * 1.60934
  end
end

function SpeedConvert(choice, value)
  if choice == 1 then
    return value / 1.60934
  elseif choice == 2 then
    return value * 1.60934
  end
end

function TempConvert(value, unit1, unit2)
  if unit1 == "C" and unit2 == "F" then
    return (value * 9 / 5) + 32
  elseif unit1 == "C" and unit2 == "K" then
    return value + 273.15
  elseif unit1 == "F" and unit2 == "C" then
    return (value - 32) * 5 / 9
  elseif unit1 == "F" and unit2 == "K" then
    return (value - 32) * 5 / 9 + 273.15
  elseif unit1 == "K" and unit2 == "C" then
    return value - 273.15
  elseif unit1 == "K" and unit2 == "F" then
    return (value - 273.15) * 9 / 5 + 32
  end
end

function Main()
  io.write("What unit do you want to convert? (length (km, miles), speed (mph, kmh), temperature (C, F, K)) ")
  local choice = io.read()

  if choice == "length" then
    io.write("enter the value of the distance to convert: ")
    local length_value = tonumber(io.read())
    io.write("do you want to convert km to miles (1) or miles to km? (2) ")
    local length_choice = tonumber(io.read())
    if length_choice == 1 then
      print(LengthConvert(1, length_value))
    elseif length_choice == 2 then
      print(LengthConvert(2, length_value))
    end
  elseif choice == "speed" then
    io.write("enter the value of the distance to convert: ")
  elseif choice == "temperature" then
    io.write("enter the value of the temperature to convert: ")
  end
end

Main()
