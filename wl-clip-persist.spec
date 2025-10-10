%bcond check 1

%global 		cargo_install_lib 0
%global         base_pkg_name wl-clip-persist

%define 		_disable_source_fetch 0

Name:           %{base_pkg_name}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Keep clipboard after program closes in wayland
License:  		MIT
URL:            https://github.com/Linus789/%{base_pkg_name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo gcc glibc

%description
Keep clipboard persistent after program closes in wayland.

%prep
%autosetup -n %{base_pkg_name}-%{version}

%build
#TODO: convert missing dependencies to rpm and redo with cargo macros
export CARGO_TARGET_DIR=target
cargo fetch --target x86_64-unknown-linux-gnu
cargo build --release --all-features

%install
install -Dm 755 target/release/%{base_pkg_name} "%{buildroot}%{_bindir}/%{base_pkg_name}"
install -Dm 644 README.md "%{buildroot}%{_datadir}/doc/%{base_pkg_name}/README.md"
install -Dm 644 LICENSE "%{buildroot}%{_datadir}/licenses/%{base_pkg_name}/LICENSE"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{base_pkg_name}

%changelog
%autochangelog
