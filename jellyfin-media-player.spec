%global         base_pkg_name jellyfin-media-player

%define _disable_source_fetch 0

Name:           %{base_pkg_name}
Version:        1.11.0
Release:        1%{?dist}
Summary:        Media Player for Jellyfin Media Server.
Url:            https://github.com/jellyfin/%{base_pkg_name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:  GPL-2.0-only

BuildRequires: pkgconfig(Qt5Core) qt5-qtbase-private-devel pkgconfig(Qt5WebChannel) pkgconfig(Qt5WebEngineWidgets) pkgconfig(Qt5X11Extras) pkgconfig(libcec) pkgconfig(mpv) pkgconfig(sdl2)
Requires: qt5-qtquickcontrols

%description
Media Player for Jellyfin Media Server.

%prep
%autosetup -n %{base_pkg_name}-%{version}

%build
%cmake -DCMAKE_SKIP_RPATH=1 -DCHECK_FOR_UPDATES=OFF -Wno-dev
%cmake_build

%install
%cmake_install

%files
%{_bindir}/jellyfinmediaplayer
%{_datadir}/jellyfinmediaplayer/web-client/extension/*
%{_datadir}/applications/com.github.iwalton3.%{base_pkg_name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.iwalton3.%{base_pkg_name}.svg
%{_datadir}/metainfo/com.github.iwalton3.jellyfin-media-player.appdata.xml

%changelog
* Thu Oct 9 2025 Donavan Campbell <vncvltvred@proton.me> - 1.12.0-1
- initial package
