*Procedural Mesh Generation*

Problem: Creating games and simulations requires a lot of art. Building 3d worlds requires considerable money and time, as 3d artists must be hired to create fully textured and rigged meshes.
If 3d meshes could be generated in a faster, more versatile, and completely reusable way, this would substantially reduce the cost and time of developing 3d applications.

Existing Software: There exists some software which provides completed models out of the box. These packages, however, do not guarantee that they will have the exact kind of model or mesh you are
looking for, and typically offer little to no customization of those models out of the box, forcing you to modify them yourself. There also exists some software for procedurally generated meshes,
however these programs are all very limited in scope, and tend to hard-code the types of procedural designs that are able to be created, due to the complexity of a customizable procedural system.

Technology: The technology that I am using to create my Procedural Mesh Generator is Unity. Unity is a very powerful engine for games and simulations. It has a long history in the indie market,
and offers a tremendous amount of customizability, as well as source code licenses when necessary. With the recent release of Unity 5, the engine is more powerful and widespread than ever,
and can deploy to nearly any platform. These factors, combined with my prior experience and comfort within the Unity engine, make it a perfect fit for my project, which will make heavy use of 
the 3d mesh modification tools that Unity has to offer.

End Product: The goal of my Procedural Mesh Generator is to offer the user the ability to define meshes based off of a generation routine, and then build them in real time using Unity's mesh class.
This project is unique in its potential and scope; generation is abstracted into several core Classes, allowing the user to specify key information, such as vertex positions or functions to map to,
and UV mapping mode, and then taking that information and building meshes from the ground up. All mesh attributes are able to be modified at random based on a specified range, allowing the user
to quickly create scenes with massive amount of detail, where no two objects look exactly alike.