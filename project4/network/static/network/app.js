
function edit_post(event) {
    event.preventDefault();

    let post_id = event.target.dataset.post_id;
    let before_content = document.querySelector(`.post-container [data-post_id="${post_id}"]:nth-child(3) span`).innerHTML;

    let edit_form = document.createElement("form");
    edit_form.setAttribute('method', 'put')
    edit_form.setAttribute('class', 'edit-form')

    let textarea = document.createElement('textarea');
    textarea.className = 'form-control form-post-content';
    textarea.id = 'exampleFormControlTextarea4';
    textarea.setAttribute('rows', '3');
    textarea.setAttribute('name', 'content');
    textarea.innerHTML = before_content.trim();

    let submit = document.createElement('input');
    submit.setAttribute('type', 'submit');
    submit.setAttribute('value', 'Save');

    edit_form.append(textarea)
    edit_form.append(submit)

    // hide preexisting content spot
    document.querySelector(`.post-container [data-post_id="${post_id}"]:nth-child(3) span`).innerHTML = '';
    document.querySelector('.edit-link').style.display = 'none';

    // append form to content upon clicking the edit button
    document.querySelector(`.post-container [data-post_id="${post_id}"]:nth-child(3)`).append(edit_form);

    document.querySelector('.edit-form input').addEventListener('click', (event) =>{
        event.preventDefault()
        // grab new content
        let new_content = document.querySelector('.edit-form textarea').value
        const csrftoken = getCookie('csrftoken')
        // fetch edit post and add content to db
        fetch('/edit_post/' + post_id, {
            method: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({
                content: new_content
            })
        })
        // delete form
        .then(document.querySelector('.edit-form').remove())
        // show edit button
        .then(document.querySelector('.edit-link').style.display = 'block')
        // add content back to span
        .then(document.querySelector(`.post-container [data-post_id="${post_id}"]:nth-child(3) span`).innerHTML = new_content)
    });
}

function like_post(event) {
    event.preventDefault()

    let csrftoken = getCookie('csrftoken')
    let id = event.target.parentNode.dataset.post_id;
    fetch('/like_post/' + id, {
        method:"POST",
        headers: {'X-CSRFToken': csrftoken}
    })
    .then(response => {
        let target_text = event.target
        let parent = event.target.parentNode;
        let likes = parent.dataset.post_likes;
        if (response.status == 202) {
            likes ++;
            event.target.className = 'btn btn-primary btn-small likes liked';
        }
        else {
            likes --;
            event.target.className = 'btn btn-primary btn-small likes unliked';
        }
        parent.dataset.post_likes = likes;
        target_text.innerHTML = `${likes} Likes`;

    })
}

function follow(event) {
    // target following and followers count in profile to update
    // update follow button to look different
    let username = event.target.parentNode.dataset.profile_user;
    let target = event.target;
    let parent = event.target.parentNode;
    console.log(parent)
    let followers = parent.dataset.follower_count;
    let followerHTML = document.querySelector('.followers span a')
    console.log(username, followers)

    fetch('follow/' + username, {
        method:"GET",
    })
    .then(response => {
        console.log(response)
        if (response.status == 202) {
            followers++;
            target.innerHTML= 'Unfollow';
            target.className = 'unfollow btn btn-primary';
        }
        else {
            followers--;
            target.innerHTML= 'Follow';
            target.className = 'follow btn btn-primary';
        }
        parent.dataset.follower_count = followers;
        console.log(parent.dataset.follower_count)
        followerHTML.innerHTML = `${followers} Followers`;


    })
}

function submit_post(event) {

    event.preventDefault()

    let content = document.querySelector('#post-content').value;
    const csrftoken = getCookie('csrftoken')

    fetch('/new_posts', {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            content: content
        })
    })
    .then(document.querySelector('.post-content').value = "")
}

// Got this code from the Django documents
// Grabs cookies based on names
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
    }
    return cookieValue
}