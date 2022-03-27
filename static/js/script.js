function toggleMobileNav(menu) {
  menu.classList.toggle("open");
}

// New Post Form, place holder over rides. 
$("input#id_title").attr("placeholder", "Enter a title...(required)");
$("input#id_live_link").attr("placeholder", "Enter a Live link...(https://...)");
$("input#id_repo_link").attr("placeholder", "Enter a Repo link...(https://...)");

// Signup form, place holder over rides 
$("input#id_repo_link").attr("placeholder", "Enter a Repo link...(https://...)");