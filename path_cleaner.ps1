# # Get the current PATH environment variable
# $path = [Environment]::GetEnvironmentVariable("Path", "User")

# # Split the PATH into individual paths
# $pathArray = $path.Split(";")

# # Create a new array to store unique paths
# $uniquePaths = @()

# # Iterate through each path and add it to the unique paths array if it's not already present
# foreach ($singlePath in $pathArray) {
#     $trimmedPath = $singlePath.Trim()
#     if ($trimmedPath -ne "" -and $uniquePaths -notcontains $trimmedPath) {
#         $uniquePaths += $trimmedPath
#     }
# }

# # Join the unique paths back into a single string
# $cleanedPath = $uniquePaths -join ";"

# # Update the PATH environment variable
# [Environment]::SetEnvironmentVariable("Path", $cleanedPath, "User")

# # Output the cleaned PATH
# Write-Host "Cleaned PATH:"
# Write-Host $cleanedPath

# $path = [System.Environment]::GetEnvironmentVariable(
#     'PATH',
#     'Machine'
# )
# # Remove unwanted elements
# $path = ($path.Split(';') | Where-Object { $_ -notcontains 'python' }) -join ';'
# # Set it
# [System.Environment]::SetEnvironmentVariable(
#     'PATH',
#     $path,
#     'Machine'
# )

$path = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$newPath = (($path -split ';') | Where-Object { $_ -notlike '*python*' }) -join ';'
[Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')
$path = [Environment]::GetEnvironmentVariable('Path', 'Machine')
Write-Host $path