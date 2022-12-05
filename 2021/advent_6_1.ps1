class fish
{   
    [int]$TimerValue
    fish([int]$timer)
    {
      $this.TimerValue = $timer
    }
    [void]NewDay()
    {
      $this.TimerValue--
    }

    [bool]IsReproducing()
    {
       return $this.TimerValue -eq 0
    }
    [fish]CreateNewFish()
    {
      $this.TimerValue = 7
      return [fish]::new(9)
    }
}

$fishList = [System.Collections.Generic.List[fish]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input6.txt')
{
   foreach($number in $line.Split(","))
   {
      $fishList.Add([fish]::new($number))
   }
}
Write-Host "Start with " $fishList.Count " fishs"

for($i=1;$i-le80;$i++)
{
  
  $newfish = [System.Collections.Generic.List[fish]]::New();
  foreach($fish in $fishList)
  {    
     $fish.NewDay() 
     if($fish.IsReproducing())
     {
        $newfish.Add($fish.CreateNewFish())
     }
     
  }
  Write-Host "Day:" $i " Fish:" $fishList.Count " New Fish:" $newfish.Count
  foreach($fish in $newfish)
  {
     $fishList.Add($fish)
  }
 
}
Write-Host "Fishis:" $fishList.Count