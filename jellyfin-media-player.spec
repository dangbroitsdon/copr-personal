%global         latest_git_commit b18c359ed70e3aece0a56b0889fd0b6464b05b8f
%global         shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})
%global         date %(date +%Y%m%d)
%global         hour %(date +%H)
%global         base_pkg_name jellyfin-media-player

%define _disable_source_fetch 0

Name:           %{base_pkg_name}
Version:        1.12.0
Release:        1%{?dist}
Summary:        Media Player for Jellyfin Media Server.
Url:            https://github.com/jellyfin/%{base_pkg_name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        GPL-3.0-or-later

BuildRequires: mpv-devel libcec-devel platform-devel SDL2-devel cmake git python g++ qt5-qtbase-devel qt5-qtbase-private-devel qt5-qtdeclarative-devel qt5-qtwebengine-devel qt5-qtx11extras-devel qt5-qtwebchannel-devel qt5-qtlocation-devel protobuf-devel libSM-devel libXext-devel libXrandr-devel minizip-ng-compat-devel

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
