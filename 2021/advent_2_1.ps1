$forward = 0
$depth = 0

foreach($line in  Get-Content 'C:\temp\advent_input2.txt')
{
         $matches = [regex]::Matches($line, "([^ ]+) ([^ ]+)")
         $direction = $matches[0].Groups[1].Value
         $step = [int]$matches[0].Groups[2].Value
         switch($direction)
         {
           "forward" { $forward += $step}
           "up" { $depth -= $step}
           "down" { $depth += $step}
         }
         if($depth -lt 0)
         {
          $depth = 0
          Write-Host "depth set to 0"
         }
}
Write-Host "Depth: "  $depth
Write-Host "Pos: " $forward
Write-host "Final:" ($depth*$forward)