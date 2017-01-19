function allerVersAncre(){
	var ancre = document.getElementById('nomAncre').value;
	var liensExistant = document.getElementsByName(ancre);
	if (liensExistant.length > 0){
		window.location = "#"+ancre;
		window.scrollBy(0,-80);
		} 
	else
		window.alert("Le verbe `" + ancre + "` n'est pas présent dans les données !\n(Est-ce la bonne orthographe ?)");
	return false; // Pour éviter de valider le formulaire
}
