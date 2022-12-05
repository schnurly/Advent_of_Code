

$fishList = New-Object int64[] 8
foreach($num in $fishList)
{ 
  $num =0
}
foreach($line in  Get-Content 'C:\temp\advent_input6_2.txt')
{
   foreach($number in $line.Split(","))
   {
      $fishList[$number]++
   }
}

$newfish = 0
for($i=0;$i-le18;$i++)
{ 
   $current0fish = $fishList[0] 
   for($j=1;$j-lt$fishList.Count;$j++)
   {
      $fishList[$j-1] =$fishList[$j]
   }
   $fishList[7] = $newfish
   $fishList[5] += $newfish
   $newfish = $current0fish
      
   $fishsum=$current0fish
   for($j=0;$j-lt$fishList.Count;$j++)
   {
      $fishsum+=$fishList[$j] 
   }
   Write-host "Day:" $i " Fish:" $fishsum 

}
