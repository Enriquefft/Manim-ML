{
  description = "Manim educational video project with uv package manager";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
  };

  outputs =
    { nixpkgs, ... }:
    let
      inherit (nixpkgs) lib;
      forAllSystems = lib.genAttrs lib.systems.flakeExposed;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.mkShell {
            buildInputs = [
              # Python and dev tools
              pkgs.python313
              pkgs.uv
              pkgs.tmux

              # Manim CLI tool (pre-built, works standalone)
              pkgs.manim
              pkgs.ffmpeg
              pkgs.sox

              # manim-voiceover dependencies
              pkgs.portaudio  # For PyAudio (voice recording)
              pkgs.gettext    # For translation support

              # Tools
              pkgs.ruff
              pkgs.pyright

              # Build tools
              pkgs.gcc
              pkgs.pkg-config
              pkgs.gnumake

              # X11 and graphics libraries (for glcontext)
              pkgs.xorg.libX11
              pkgs.libGL

              # Pango and Cairo (for manimpango)
              pkgs.pango
              pkgs.cairo

              # Development tools
              pkgs.git
              pkgs.pre-commit
            ];

            shellHook = ''
              unset PYTHONPATH
              uv sync
              . .venv/bin/activate
              # Make manim CLI available
              export PATH="${pkgs.manim}/bin:$PATH"
              # Add project root to PYTHONPATH for src imports
              export PYTHONPATH="$PWD:$PYTHONPATH"
            '';
          };
        }
      );
    };
}
