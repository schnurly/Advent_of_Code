class Node
{
  [string]$Name
  [System.Collections.Generic.List[Node]]$Connected
  Node()
  {
     $this.Connected =[System.Collections.Generic.List[Node]]::New();
  }
  [bool] IsBigCave()
  {
    return $($this.Name) -cmatch "[A-Z]+"
  }

}

$foundPath = [System.Collections.Generic.List[String]]::new();


function TraversePath([Node] $node,[System.Collections.Generic.List[String]] $path,[bool] $isTwice)
{
    $path.Add($node.Name)
    if($node.Name -eq "end")
    {
       if(!$foundPath.Contains([String]::Join(",",$path)))
      {
      Write-host "PathFound:" $([String]::Join(",",$path))   
      $foundPath.Add($([String]::Join(",",$path)))
      }
      return 
    }
    foreach($childNode in $node.Connected)
    {
       $tmpIsTwice = $isTwice
       if($childNode.Name -ne "start")
       {   
           $foundCount=0
             if(!$childNode.IsBigCave())
             {
                 foreach($subPath in $path)
                 {
                    if($subPath -eq $childNode.Name)
                    {
                      $foundCount++
                    }
                 }               
                 if($foundCount -gt 1 )
                 {                    
                   continue               
                 }  
                 elseif($foundCount -eq 1 -and $tmpIsTwice -eq $false)
                 {
                   $tmpIsTwice  = $true
                 }
                 elseif($foundCount -eq 1 -and $tmpIsTwice -eq $true)
                 {
                   continue
                 }
                                             
             }
         
             
             $newpath = [System.Collections.Generic.List[String]]::New()
             $newpath.AddRange($path.ToArray())
             #Write-host "Traverse from " $node.Name " to " $childNode.Name
             #Write-Host "Path:" $([String]::Join(",",$path))

             TraversePath $childNode $newpath $tmpIsTwice         
           
       }
    }
}

$nodes = [System.Collections.Generic.Dictionary[[String],Node]]::New();


foreach($line in  Get-Content 'C:\temp\advent_input12.txt')
{
   $arr = $line.split("-")
   foreach($field in $arr)
   {
     if(!$nodes.ContainsKey($field))
     {
         $node = [Node]::New();
         $node.Name = $field
         $nodes.Add($field, $node)
     }
   }
   $nodes[$arr[0]].Connected.Add($nodes[$arr[1]])
   $nodes[$arr[1]].Connected.Add($nodes[$arr[0]])
}


$path  =[System.Collections.Generic.List[String]]::New();

TraversePath $nodes["start"] $path $false
Write-Host "FoundPath:" $foundPath.Count