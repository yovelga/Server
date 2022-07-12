function fetch_users_fe() {
    console.log("123")
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response => get_user_fe(response.data)
    ).catch(
        err => console.log(err)
    );
}


function get_user_fe(response){
    const currMain = document.querySelector("main")
    const user_id = document.getElementById("user_num_fetch_fe").value;
    let i = 0;
    var fetch_fe_results = document.getElementById("fetch_fe_results");
    fetch_fe_results.innerHTML = "";//remove all child elements inside of myDiv


    if (user_id == 0){
        i = 0;
        for (let user of response){
            console.log(user)
            const section = document.createElement('section')
            section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${ user.email}">Send Email</a>
            </div>
        `
            currMain.appendChild(section)
        }
    }


    for (let user of response){
        console.log(user)
        i += 1;
        const section = document.createElement('section')

        if (user_id == i)
            section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <span>${user.last_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}">Send Email </a>
             <br><br>
            </div>
        `
        currMain.appendChild(section)
    }

}



