
$sorted = @()
$fuel = @()
$unordered = [System.Collections.Generic.List[int]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input7.txt')
{
   foreach($number in $line.Split(","))
   {
      $unordered.Add($number)
   }
}
$highestnum = 0;
foreach($num in $unordered)
{
   if($num -gt $highestnum)
   {
     $highestnum = $num
   }
}
$passfuelcost = @()
Write-Host "HighestNum:" $highestnum
for($i=0;$i-le$highestnum;$i++)
{
  $sorted+=0
  $fuel+=0
  $passfuelcost+=fuel $i
}
foreach($num in $unordered)
{
    $sorted[$num]++
}

Function fuel([int]$passes)
{
   $retVal = 0
   for($i=1;$i-le$passes;$i++)
   {
      $retVal+=$i
   }

   return $retVal
}



for($targetLine=0;$targetLine-le$highestnum;$targetLine++)
{
   for($i=0;$i-le$highestnum;$i++)
   {
      $usedFuel = $i -$targetLine
      if($usedFuel -lt 0)
      {
        $usedFuel *=-1
      }
      $newfuel = $passfuelcost[$usedFuel]
      $fuel[$targetLine]+= ( $newfuel * $sorted[$i])
   }
}

$lowestline=0
for($i=0;$i-le$highestnum;$i++)
{
   Write-Host "Line:" $i " Fuel:"  $fuel[$i]
   if($fuel[$lowestline] -gt $fuel[$i])
   {
      $lowestline=$i
   }
}

Write-Host "Best line " $lowestline " Fuel used:" $fuel[$lowestline]