export const siteConfig = {
  name: "SnapJobs",
  links: {
    twitter: "https://twitter.com/iamvinitk",
    github: "https://github.com/snapjobs-me",
  },
  routes: {
    home: "/",
    about: "/about",
    contact: "/contact",
    blog: "/blog",
    jobs: "/jobs",
    search: "/search",
    login: "/login",
    applications: "/applications",
    snapAI: "/snapai",
  },
  api: "http://localhost:8000",
};

export type SiteConfig = typeof siteConfig;
