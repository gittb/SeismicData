# SeismicData
VandyHacks 2018 Best Overall Project
Inspiration

Some problems have become so ingrained within our society that they go all-but unnoticed, even as they lie in our plain sight. The way we use public video surveillance today is one of these problems: We accept its potential to violate our privacy, its unsuitability for data collection, and its great expense because we believe it to be our only option. This is no longer the case. Seismic Data is a proof of concept for an audio-based surveillance system that answers each of these issues while providing opportunities far beyond its elementary security applications.


What it does
---------------

Seismic’s use of audio for surveillance is simultaneously more effective and less invasive than video. By triangulating the origin of every sound impulse travelling through the ground, it can track every moving object within a confined space, regardless of obstacles that would interrupt a camera’s line of sight. The locations 


How we built it
----------------
In abstract, Seismic applies an already-established mathematical system, originally developed to triangulate the position of military artillery, but on a relatively smaller scale. Using only the time it takes a sound to reach an array of three microphones, Seismic can theoretically detect the source of any vibration within a confined area of uniform material. It is built using Python, C++, Microcontrollers, Tensorflow, love and Caffeine.


Challenges we ran into
-----------------
After one round of testing, we quickly realized that a sound impulse is much harder to detect over a short distance, in a material, than over a long distance in air. While the sound of artillery fire may pass by a sensor in one easy-to-define instant, making triangulation a simple matter of algebra and geometry, footsteps do not reach our sensors in one distinguishable moment and cannot be used mathematically except by a machine-learning algorithm. So what we thought was a simple system of equations became a major technical challenge that we could not fully overcome within our constraints. We also struggled with our own inexperience using many of our technical systems: Teaching each other Python, Matlab, and trigonometry was a significant time investment.
