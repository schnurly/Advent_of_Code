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


function TraversePath([Node] $node,[System.Collections.Generic.List[String]] $path )
{
    $path.Add($node.Name)
    if($node.Name -eq "end")
    {
      Write-host "PathFound:" $([String]::Join(",",$path))
      $foundPath.Add($([String]::Join(",",$path)))
      return 
    }
    foreach($childNode in $node.Connected)
    {
       if($childNode.Name -ne "start")
       {
           if(!$childNode.IsBigCave())
           {
             $found = $false
             foreach($subPath in $path)
             {
                if($subPath -eq $childNode.Name)
                {
                  $found = $true
                }
             }
             if($found -eq $true)
             {
               continue
             }          
           }      
             $newpath = [System.Collections.Generic.List[String]]::New()
             $newpath.AddRange($path.ToArray())
             #Write-host "Traverse from " $node.Name " to " $childNode.Name
             #Write-Host "Path:" $([String]::Join(",",$path))
             TraversePath $childNode $newpath         
        
       }
    }
}

$nodes = [System.Collections.Generic.Dictionary[[String],Node]]::New();


foreach($line in  Get-Content 'C:\temp\advent_input12_2.txt')
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

TraversePath $nodes["start"] $path
Write-Host "FoundPath:" $foundPath.Count