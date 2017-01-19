function flipflop(id)
{
if (document.getElementById(id).style.display == "none")
document.getElementById(id).style.display = "block";
else	document.getElementById(id).style.display = "none";
}

function flipflopON(id1,id2)
{
if (document.getElementById(id1).style.display == "none") {
document.getElementById(id1).style.display = "block";
document.getElementById(id2).style.display = "none";
}
else	{document.getElementById(id1).style.display = "none";
document.getElementById(id2).style.display = "block";
}
}
function flipflopOFF(id1,id2)
{
if (document.getElementById(id1).style.display == "none") {
document.getElementById(id1).style.display = "block";
document.getElementById(id2).style.display = "none";
}
else	{document.getElementById(id1).style.display = "block";
document.getElementById(id2).style.display = "none";
}
}