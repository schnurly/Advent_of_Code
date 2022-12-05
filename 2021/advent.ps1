$increasedCount = 0;
$lineCount = 0;

$before=0;
foreach($line in  Get-Content 'C:\temp\advent_input.txt')
{
   if($before -ne 0)
   {
     if([int]$line -gt [int]$before)
     {
        $increasedCount++;
        $matched = $false;
        if($line -gt $before)
        { 
          $matched = $true;
         
        }
        if($matched -eq $false)
        {
         Write-Host $line " | " $before
        }
     }
   }
   $before = $line;
   $lineCount++;
}
Write-Host "Lines: " $lineCount;
Write-Host "Increased: " $increasedCount;