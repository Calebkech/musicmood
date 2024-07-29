document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[id^="menu-button-"]').forEach(button => {
        button.addEventListener('click', function () {
            const menuId = button.id.replace('menu-button-', 'dropdown-menu-');
            const menu = document.getElementById(menuId);
            menu.classList.toggle('hidden');
        });
    });

    document.addEventListener('click', function (event) {
        if (!event.target.closest('[id^="menu-button-"]') && !event.target.closest('[id^="dropdown-menu-"]')) {
            document.querySelectorAll('[id^="dropdown-menu-"]').forEach(menu => {
                menu.classList.add('hidden');
            });
        }
    });

    let currentTrackIndex = 0;
    let tracks = [];
    let userStartedPlaying = false;

    document.querySelectorAll(".play-button").forEach((button, index) => {
        tracks.push({
            url: button.getAttribute("data-url"),
            title: button.getAttribute("data-title"),
            artist: button.getAttribute("data-artist"),
            cover: button.closest(".song-item").querySelector("img").src,
        });

        button.addEventListener("click", () => {
            currentTrackIndex = index;
            playTrack();
            userStartedPlaying = true;
        });
    });

    function playTrack() {
        let track = tracks[currentTrackIndex];
        $("#jquery_jplayer").jPlayer("setMedia", {
            title: track.title,
            artist: track.artist,
            mp3: track.url,
        }).jPlayer("play");

        document.querySelector(".jp-title").textContent = `${track.title} - ${track.artist}`;
        document.getElementById("jp_cover").src = track.cover;
        document.querySelector(".jp-play").classList.add("hidden");
        document.querySelector(".jp-pause").classList.remove("hidden");
    }

    $("#jquery_jplayer").jPlayer({
        ready: function () {
            // Do not auto-play on load
        },
        swfPath: "/js",
        supplied: "mp3",
        cssSelectorAncestor: "#jp_container",
        useStateClassSkin: true,
        autoBlur: false,
        smoothPlayBar: true,
        keyEnabled: true,
        remainingDuration: true,
        toggleDuration: true,
        ended: function () {
            if (userStartedPlaying) {
                nextTrack();
            }
        }
    });

    function nextTrack() {
        currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
        playTrack();
    }

    function prevTrack() {
        currentTrackIndex = (currentTrackIndex - 1 + tracks.length) % tracks.length;
        playTrack();
    }

    document.querySelector(".jp-next").addEventListener("click", function () {
        nextTrack();
    });

    document.querySelector(".jp-previous").addEventListener("click", function () {
        prevTrack();
    });

    document.querySelector(".jp-play").addEventListener("click", function () {
        $("#jquery_jplayer").jPlayer("play");
        this.classList.add("hidden");
        document.querySelector(".jp-pause").classList.remove("hidden");
    });

    document.querySelector(".jp-pause").addEventListener("click", function () {
        $("#jquery_jplayer").jPlayer("pause");
        this.classList.add("hidden");
        document.querySelector(".jp-play").classList.remove("hidden");
    });

    document.querySelector(".jp-stop").addEventListener("click", function () {
        $("#jquery_jplayer").jPlayer("stop");
        document.querySelector(".jp-play").classList.remove("hidden");
        document.querySelector(".jp-pause").classList.add("hidden");
    });
});
