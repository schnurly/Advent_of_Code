
$count =0
foreach($line in  Get-Content 'C:\temp\advent_input8.txt')
{
   Write-Host "Block:" $line
   $block = $line.Split("|")
   Write-Host "Right:" $block[1]
   foreach($number in $block[1].Split(" "))
   {
      $length = $number.Trim().Length
      Write-Host "Length:" $length "Text:" $number
      if($length -eq 2 -or $length -eq 3 -or $length -eq 4 -or $length -eq 7)
      {
         $count++
      }
   }
}
Write-Host "count:" $count

