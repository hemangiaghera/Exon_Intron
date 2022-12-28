
basepair="AGTCGTATGCATGCATGCGTGCATGCAGTGACTGCA"
Intron= basepair[12:27]
Exon1= basepair[0:12]
Exon2= basepair[27: ]
Intronlower= Intron.lower()
print(Exon1 + Intronlower + Exon2)