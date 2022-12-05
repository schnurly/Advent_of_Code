$forward = 0
$depth = 0
$aim = 0

foreach($line in  Get-Content 'C:\temp\advent_input2.txt')
{
         $matches = [regex]::Matches($line, "([^ ]+) ([^ ]+)")
         $direction = $matches[0].Groups[1].Value
         $step = [int]$matches[0].Groups[2].Value
         switch($direction)
         {
           "forward" { 
             $forward += $step
             $depth += ($aim*$step)
             }
           "up" { $aim -= $step}
           "down" { $aim += $step}
         }
         if($aim -lt 0)
         {
          $aim = 0
          Write-Host "depth set to 0"
         }
}
Write-Host "Depth: "  $depth
Write-Host "Pos: " $forward
Write-host "Final:" ($depth*$forward)