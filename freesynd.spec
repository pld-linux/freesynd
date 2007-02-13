# TODO: optflags
Summary:	Reimplementation of the classic Bullfrog game, Syndicate
Summary(pl.UTF-8):	Reimplementacja klasycznej gry Syndicate firmy Bullfrog
Name:		freesynd
Version:	0.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freesynd/%{name}-%{version}.zip
# Source0-md5:	9efc6437d3983bdab5c28e4535c4b078
Patch0:		%{name}-FHS.patch
URL:		http://freesynd.sourceforge.net/
BuildRequires:	SDL_mixer-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeSynd is a reimplementation of the classic Bullfrog game,
Syndicate.

%description -l pl.UTF-8
FreeSynd to reimplementacja klasycznej gry Syndicate firmy Bullfrog.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -C src \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -a data $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
