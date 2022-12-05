
$listOxy = [System.Collections.Generic.List[string]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input3.txt')
{
 $listOxy.Add($line)
}
for($i=0;$i-lt12;$i++)
{
    $tmplistOxy = [System.Collections.Generic.List[string]]::New();
    $count=0
    foreach($line in  $listOxy)
    {   
       $charArray = $line.toCharArray()   
       if($charArray[$i] -eq "1")
       {
          $count++
       }             
    }

    $mid =  $listOxy.Count / 2
    if(($mid * 2) -ne  $listOxy.Count)
    {
       $mid +=1
    }

    $keep=""
    if($count -ge $mid)
    {
      $keep="1"
    }
    else
    {
       $keep="0"
    }
    foreach($line in  $listOxy)
    {   
       $charArray = $line.toCharArray()   
       if($charArray[$i] -eq $keep)
       {
          $tmplistOxy.Add($line)
       }             
    }
 
    $listOxy = $tmplistOxy
    if($listOxy.Count -eq 1)
    {
       break
    }
}


Write-Host $listOxy.Count
$gamma = $listOxy[0]

$listOxy = [System.Collections.Generic.List[string]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input3.txt')
{
 $listOxy.Add($line)
}
for($i=0;$i-lt12;$i++)
{
    $tmplistOxy = [System.Collections.Generic.List[string]]::New();
    $count=0
    foreach($line in  $listOxy)
    {   
       $charArray = $line.toCharArray()   
       if($charArray[$i] -eq "1")
       {
          $count++
       }             
    }

    $mid =  $listOxy.Count / 2
    if(($mid * 2) -ne  $listOxy.Count)
    {
       $mid +=1
    }

    $keep=""
    if($count -ge $mid)
    {
      $keep="0"
    }
    else
    {
       $keep="1"
    }
    foreach($line in  $listOxy)
    {   
       $charArray = $line.toCharArray()   
       if($charArray[$i] -eq $keep)
       {
          $tmplistOxy.Add($line)
       }             
    }
 
    $listOxy = $tmplistOxy
    if($listOxy.Count -eq 1)
    {
       break
    }
}
Write-Host $listOxy.Count
$espilon = $listOxy[0]

Write-Host $gamma
$gammeInt = [convert]::ToInt32($gamma,2)

Write-Host $espilon
$espilonInt = [convert]::ToInt32($espilon,2)

Write-Host ($gammeInt *$espilonInt)