
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
Write-Host "HighestNum:" $highestnum
for($i=0;$i-le$highestnum;$i++)
{
  $sorted+=0
  $fuel+=0
}
foreach($num in $unordered)
{
    $sorted[$num]++
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
      $fuel[$targetLine]+= ($usedFuel * $sorted[$i])
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