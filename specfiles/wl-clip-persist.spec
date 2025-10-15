%bcond check 1

%global 		cargo_install_lib 0

%define 		_disable_source_fetch 0

Name:           wl-clip-persist
Version:        0.5.0
Release:        1%{?dist}
Summary:        Keep clipboard after program closes in wayland
License:  		MIT
URL:            https://github.com/Linus789/wl-clip-persist
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo gcc glibc

%description
Keep clipboard persistent after program closes in wayland.

%prep
%autosetup -n %{name}-%{version}

%build
#TODO: convert missing dependencies to rpm and redo with cargo macros
export CARGO_TARGET_DIR=target
cargo fetch --target x86_64-unknown-linux-gnu
cargo build --release --all-features

%install
install -Dm 755 target/release/%{name} "%{buildroot}%{_bindir}/%{name}"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
