%define     _disable_source_fetch 0

Name:           mesa
Summary:        Mesa graphics libraries
Version:        25.2.5
Release:        %autorelease
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            https://gitlab.freedesktop.org/mesa/mesa
Source0:        https://archive.mesa3d.org/mesa-%{version}.tar.xz

BuildRequires:  meson >= 1.3.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kernel-headers
BuildRequires:  systemd-devel
# We only check for the minimum version of pkgconfig(libdrm) needed so that the
# SRPMs for each arch still have the same build dependencies. See:
# https://bugzilla.redhat.com/show_bug.cgi?id=1859515
BuildRequires:  pkgconfig(libdrm) >= 2.4.122
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-client) >= 1.11
BuildRequires:  pkgconfig(wayland-server) >= 1.11
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xdamage) >= 1.1
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcb-glx) >= 1.8.1
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2) >= 1.8
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(dri2proto) >= 2.8
BuildRequires:  pkgconfig(glproto) >= 1.4.14
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  lm_sensors-devel
BuildRequires:  pkgconfig(vdpau) >= 1.1
BuildRequires:  pkgconfig(libva) >= 0.38.0
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libglvnd) >= 1.3.2
BuildRequires:  llvm-devel >= 7.0.0
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-pycparser
BuildRequires:  python3-pyyaml
BuildRequires:  vulkan-headers
BuildRequires:  glslang
BuildRequires:  pkgconfig(vulkan)

%description
%{summary}.

%package filesystem
Summary:        Mesa driver filesystem
Provides:       mesa-dri-filesystem = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-omx-drivers < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-libd3d < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-libd3d-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-vdpau-drivers < %{?epoch:%{epoch}:}%{version}-%{release}

%description filesystem
%{summary}.

%package libGL
Summary:        Mesa libGL runtime libraries
Requires:       libglvnd-glx%{?_isa} >= 1:1.3.2
Requires:       %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-libOSMesa < 25.1.0~rc2-1

%description libGL
%{summary}.

%package libGL-devel
Summary:        Mesa libGL development package
Requires:       (%{name}-libGL%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-libGL%{?_isa})
Requires:       libglvnd-devel%{?_isa} >= 1:1.3.2
Provides:       libGL-devel
Provides:       libGL-devel%{?_isa}
Recommends:     gl-manpages
Obsoletes:      %{name}-libOSMesa-devel < 25.1.0~rc2-1

%description libGL-devel
%{summary}.

%package libEGL
Summary:        Mesa libEGL runtime libraries
Requires:       libglvnd-egl%{?_isa} >= 1:1.3.2
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libEGL
%{summary}.

%package libEGL-devel
Summary:        Mesa libEGL development package
Requires:       (%{name}-libEGL%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-libEGL%{?_isa})
Requires:       libglvnd-devel%{?_isa} >= 1:1.3.2
Requires:       %{name}-khr-devel%{?_isa}
Provides:       libEGL-devel
Provides:       libEGL-devel%{?_isa}

%description libEGL-devel
%{summary}.

%package dri-drivers
Summary:        Mesa-based DRI drivers
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-va-drivers%{?_isa}
Obsoletes:      %{name}-libglapi < 25.0.0~rc2-1
Provides:       %{name}-libglapi >= 25.0.0~rc2-1

%description dri-drivers
%{summary}.

%package        va-drivers
Summary:        Mesa-based VA-API video acceleration drivers
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-vaapi-drivers < 22.2.0-5

%description va-drivers
%{summary}.

%package        vdpau-drivers
Summary:        Mesa-based VDPAU drivers
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description vdpau-drivers
%{summary}.

%package libgbm
Summary:        Mesa gbm runtime library
Provides:       libgbm
Provides:       libgbm%{?_isa}
Recommends:     %{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# If mesa-dri-drivers are installed, they must match in version. This is here to prevent using
# older mesa-dri-drivers together with a newer mesa-libgbm and its dependants.
# See https://bugzilla.redhat.com/show_bug.cgi?id=2193135 .
Requires:       (%{name}-dri-drivers%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} if %{name}-dri-drivers%{?_isa})

%description libgbm
%{summary}.

%package libgbm-devel
Summary:        Mesa libgbm development package
Requires:       %{name}-libgbm%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libgbm-devel
Provides:       libgbm-devel%{?_isa}

%description libgbm-devel
%{summary}.

%package vulkan-drivers
Summary:        Mesa Vulkan drivers
Requires:       vulkan%{_isa}
Requires:       %{name}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      mesa-vulkan-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description vulkan-drivers
The drivers with support for the Vulkan API.

%prep
%autosetup -n %{name}-%{version}

%build
%define _lto_cflags %{nil}

%meson \
  -Dplatforms=x11,wayland \
  -Dgallium-drivers=llvmpipe,virgl,radeonsi,zink \
  -Dgallium-vdpau=enabled \
  -Dgallium-va=enabled \
  -Dgallium-mediafoundation=disabled \
  -Dteflon=false \
  -Dvideo-codecs=all \
  -Dvulkan-drivers=swrast,amd,virtio \
  -Dvulkan-layers=device-select \
  -Dgles1=enabled \
  -Dgles2=enabled \
  -Dopengl=true \
  -Dgbm=enabled \
  -Dglx=dri \
  -Degl=enabled \
  -Dglvnd=enabled \
  -Dintel-rt=disabled \
  -Dmicrosoft-clc=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=disabled \
  -Dbuild-tests=false \
  -Dlibunwind=enabled \
  -Dlmsensors=enabled \
  -Dandroid-libbacktrace=disabled \
%ifarch %{ix86}
  -Dglx-read-only-text=true \
%endif
  %{nil}
%meson_build

%install
%meson_install

# libvdpau opens the versioned name, don't bother including the unversioned
rm -vf %{buildroot}%{_libdir}/vdpau/*.so

# likewise glvnd
rm -vf %{buildroot}%{_libdir}/libGLX_mesa.so
rm -vf %{buildroot}%{_libdir}/libEGL_mesa.so
# XXX can we just not build this
rm -vf %{buildroot}%{_libdir}/libGLES*

# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s %{_libdir}/libGLX_mesa.so.0 %{buildroot}%{_libdir}/libGLX_system.so.0

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd %{buildroot}%{_libdir}
for i in libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd

%files filesystem
%dir %{_libdir}/dri
%dir %{_datadir}/drirc.d

%files libGL
%{_libdir}/libGLX_mesa.so.0*
%{_libdir}/libGLX_system.so.0*
%files libGL-devel
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/pkgconfig/dri.pc

%files libEGL
%{_datadir}/glvnd/egl_vendor.d/50_mesa.json
%{_libdir}/libEGL_mesa.so.0*
%files libEGL-devel
%dir %{_includedir}/EGL
%{_includedir}/EGL/eglext_angle.h
%{_includedir}/EGL/eglmesaext.h

%files libgbm
%{_libdir}/libgbm.so.1
%{_libdir}/libgbm.so.1.*
%files libgbm-devel
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_includedir}/gbm_backend_abi.h
%{_libdir}/pkgconfig/gbm.pc

%files dri-drivers
%{_datadir}/drirc.d/00-mesa-defaults.conf
%{_libdir}/libgallium-*.so
%{_libdir}/gbm/dri_gbm.so
%{_libdir}/dri/kms_swrast_dri.so
%{_libdir}/dri/libdril_dri.so
%{_libdir}/dri/swrast_dri.so
%{_libdir}/dri/virtio_gpu_dri.so
%{_libdir}/dri/radeonsi_dri.so
%{_libdir}/dri/zink_dri.so

%files va-drivers
%{_libdir}/dri/radeonsi_drv_video.so
%{_libdir}/dri/virtio_gpu_drv_video.so

%files vdpau-drivers
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/libvdpau_radeonsi.so.1*
%{_libdir}/vdpau/libvdpau_virtio_gpu.so.1*

%files vulkan-drivers
%{_libdir}/libvulkan_lvp.so
%{_datadir}/vulkan/icd.d/lvp_icd.*.json
%{_libdir}/libVkLayer_MESA_device_select.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
%{_libdir}/libvulkan_virtio.so
%{_datadir}/vulkan/icd.d/virtio_icd.*.json
%{_libdir}/libvulkan_radeon.so
%{_datadir}/drirc.d/00-radv-defaults.conf
%{_datadir}/vulkan/icd.d/radeon_icd.*.json

%changelog
%autochangelog
