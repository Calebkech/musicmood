# MusicMood

MusicMood is a web application designed to provide personalized music recommendations based on the user's current mood. Our goal is to enhance the music listening experience by leveraging mood-based algorithms to suggest songs that align with the user's emotions.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Purpose](#project-purpose)
3. [Team Members](#team-members)
4. [Target Audience](#target-audience)
5. [Personal Focus](#personal-focus)
6. [Technologies Used](#technologies-used)
7. [Features](#features)
8. [Challenges](#challenges)
9. [Installation](#installation)
10. [Usage](#usage)
11. [Contributing](#contributing)
12. [License](#license)
13. [Contact](#contact)

## Introduction

![MusicMood Logo](insert_screenshot_or_logo_here)

MusicMood provides personalized music recommendations based on user moods. By integrating the Spotify API, the application delivers tailored playlists that match the user's emotional state, enhancing their music listening experience.

## Project Purpose

The purpose of MusicMood is to make music discovery more intuitive and enjoyable by suggesting songs that resonate with the user's current mood. Whether the user is feeling happy, sad, energetic, or relaxed, MusicMood aims to provide the perfect soundtrack.

## Team Members

- **Caleb:** Backend Developer
- **Aymanne:** Frontend Developer

## Target Audience

MusicMood is designed for music enthusiasts who enjoy discovering new songs that match their emotional state. It is ideal for anyone looking to enhance their daily activities with music that complements their mood.

## Personal Focus

My primary focus was on integrating the frontend with the backend, ensuring seamless data flow, and developing the mood-based recommendation algorithm. I also worked closely with the team to debug issues and refine the database schema to support our application's functionalities.

## Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **API Integration:** Spotify API
- **Authentication:** OAuth

## Features

1. **User Authentication:** Secure login and registration using OAuth.
2. **Mood-Based Recommendations:** Suggests songs based on the user's current mood.
3. **Playlist Management:** Allows users to create and manage their playlists.

## Challenges

### Technical Challenges

1. **Integration Complexity:** Integrating the frontend with the backend led to data handling issues. Additional time was spent debugging and improving error handling mechanisms.
2. **Database Schema Adjustments:** The initial database schema was inadequate for all functionalities, leading to schema refinements and optimized queries.
3. **Recommendation Algorithm Complexity:** Creating an effective mood-based recommendation algorithm was challenging. This was broken down into smaller parts, with plans for iterative improvements based on user feedback.

### Non-Technical Challenges

1. **Team Coordination:** Coordinating across different schedules and time zones was difficult, necessitating increased check-ins and the use of collaboration tools.
2. **User Interface Design:** Designing an intuitive UI took more time than planned. The initial design was simplified, with plans for iterative improvements based on user feedback.
3. **Scope Management:** Avoiding feature creep was challenging. MVP features were prioritized, and new ideas were documented for future iterations.

## Installation

To run MusicMood locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/musicmood.git
   cd musicmood
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the application:**
   ```sh
   flask run
   ```

## Usage

1. **Sign Up:** Create a new account by providing your username, email, password, and other details.
2. **Log In:** Log into your account to access personalized music recommendations.
3. **Update Profile:** Update your profile information, including uploading a profile picture.
4. **Add Songs:** Add songs to the database with details like title, artist, album, genre, and release date.
5. **Create Playlists:** Create and manage playlists based on your mood.
6. **Browse Songs and Playlists:** Browse through the songs and playlists available in the application.

## Contributing

We welcome contributions to MusicMood. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

MusicMood is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or feedback, please contact us:

- **GitHub:** [GitHub Profile](https://github.com/calebkech)
