$increasedCount = 0;
$lineCount = 0;


$lines = Get-Content 'C:\temp\advent_input.txt';

for($i=0; $i -lt $lines.count; $i++)
{
   if($i+3 -lt $lines.count)
   {
    
      $val2 = [int]$lines[$i +1 ] + [int]$lines[$i +2] + [int]$lines[$i +3];
      $val1 = [int]$lines[$i] + [int]$lines[$i +1] + [int]$lines[$i +2];
      Write-Host $val2  " - " $val1
      if($val2 -gt $val1)
      {
      
        $increasedCount++;
      }
   }
   $lineCount++;
}
Write-Host "Lines: " $lineCount;
Write-Host "Increased: " $increasedCount;