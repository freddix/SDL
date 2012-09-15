Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	1.2.15
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	9d96df8417572a2afb781a7c4c811a85
URL:		http://www.libsdl.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-modules
#BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-proto
BuildRequires:	yasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%package devel
Summary:	SDL - Header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
SDL - Header files.

%prep
%setup -q

: > acinclude.m4
echo 'AC_DEFUN([AM_PATH_ESD],[$3])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-rpath			\
	--disable-static		\
	--enable-dga			\
	--enable-nasm			\
	--enable-pthread-sem		\
	--enable-pthreads		\
	--enable-video-dga		\
	--enable-video-fbcon		\
	--enable-video-opengl		\
	--enable-video-x11-dgamouse	\
	--enable-video-x11-vm		\
	--enable-video-x11-xinerama	\
	--enable-video-x11-xme		\
	--enable-video-x11-xrandr	\
	--enable-video-x11-xv		\
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -rf docs/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS README TODO WhatsNew
%attr(755,root,root) %ghost %{_libdir}/libSDL-*.so.?
%attr(755,root,root) %{_libdir}/libSDL-*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/libSDL.so
%{_libdir}/libSDL.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/sdl.m4
%{_pkgconfigdir}/sdl.pc
%{_mandir}/man3/*

