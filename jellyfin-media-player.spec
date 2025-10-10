%global         latest_git_commit b18c359ed70e3aece0a56b0889fd0b6464b05b8f
%global         shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})
%global         date %(date +%Y%m%d)
%global         hour %(date +%H)
%global         base_pkg_name jellyfin-media-player

%define _disable_source_fetch 0

Name:           %{base_pkg_name}
Version:        1.12.0
Release:        1%{?dist}
Summary:        PDF viewer with a focus on textbooks and research papers.
Url:            https://github.com/jellyfin/%{base_pkg_name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        GPL-3.0-or-later

BuildRequires: mpv-devel libcec-devel platform-devel SDL2-devel cmake git python g++ qt5-qtbase-devel qt5-qtbase-private-devel qt5-qtwebengine-devel qt5-qtx11extras-devel

%description
Sioyek is a PDF viewer with a focus on textbooks and research papers.

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
* Sun Jul 27 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+20250727.13.8d173d9-2
- build against mupdf 1.26 and minor change

* Sat Apr 05 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+20250405.18.957f1dd-1
- update versioning

* Fri Apr 04 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git3172c42-1
- simple changes in line with fedora packaging guidelines

* Mon Mar 31 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git4ee8831-1
- misc changes

* Wed Mar 12 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+gitb3575d9-1
- Further cleanup

* Fri Feb 28 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-4
- Cleanup build and file section

* Wed Feb 26 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-3
- Fix icon not being able to be replaced by papirus-icons

* Tue Feb 25 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-2
- Fix missing icon

* Fri Feb 21 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-1
- First release and initial testing
